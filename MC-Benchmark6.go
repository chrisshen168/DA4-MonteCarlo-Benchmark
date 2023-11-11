package main

import (
	"database/sql"
	"encoding/csv"
	"fmt"
	"io"
	"log"
	"os"
	"strings"
	"time"

	_ "github.com/mattn/go-sqlite3"
)

func main() {
	db, err := sql.Open("sqlite3", "testGoDBlite6.db")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	tables := []struct {
		name     string
		datatype string
	}{
		{"dec02mb01", "float"},
		{"dec04mb01", "float"},
		{"dec08mb01", "float"},
		{"dec16mb01", "float"},
		{"geo02mb01", "point"},
		{"geo04mb01", "point"},
		{"geo08mb01", "point"},
		{"geo16mb01", "point"},
		{"int02mb01", "int"},
		{"int04mb01", "int"},
		{"int08mb01", "int"},
		{"int16mb01", "int"},
		{"json02mb01", "json"},
		{"json04mb01", "json"},
		{"json08mb01", "json"},
		{"json16mb01", "json"},
		{"text02mb01", "text"},
		{"text04mb01", "text"},
		{"text08mb01", "text"},
		{"text16mb01", "text"},
	}

	numCycles := 100

	for _, table := range tables {
		runCRUDOperations(db, table.name, table.datatype, numCycles)
	}
}

func runCRUDOperations(db *sql.DB, tableName, datatype string, numCycles int) {
	var createTimes, readTimes, updateTimes, createTimes2, updateTimesOverall, deleteTimes, totalTimes []float64

	for i := 0; i < numCycles; i++ {
		start1 := time.Now()
		createTableLite(db, tableName, datatype)
		insertDataLite(db, tableName)
		start2 := time.Now()

		createTime := start2.Sub(start1).Seconds()
		createTimes = append(createTimes, createTime)

		start3 := time.Now()
		readAllRecordsLite(db, tableName)
		start4 := time.Now()

		readTime := start4.Sub(start3).Seconds()
		readTimes = append(readTimes, readTime)

		tableName2 := strings.ReplaceAll(tableName, "01", "02")
		start5 := time.Now()
		createTableLite(db, tableName2, datatype)
		insertDataLite(db, tableName2)
		start6 := time.Now()

		createTime2 := start6.Sub(start5).Seconds()
		createTimes2 = append(createTimes2, createTime2)

		start7 := time.Now()
		updateRecordLite(db, tableName, tableName2, datatype)
		start8 := time.Now()

		updateTime := start8.Sub(start7).Seconds()
		updateTimes = append(updateTimes, updateTime)

		updateTimeOverall := start8.Sub(start5).Seconds()
		updateTimesOverall = append(updateTimesOverall, updateTimeOverall)

		start9 := time.Now()
		tryDeleteAllRecordsLite(db, tableName)
		start10 := time.Now()

		deleteTime := start10.Sub(start9).Seconds()
		deleteTimes = append(deleteTimes, deleteTime)

		totalTime := start10.Sub(start1).Seconds()
		totalTimes = append(totalTimes, totalTime)
	}

	fmt.Printf("Average Create time for %s over %d cycles: %.2f seconds\n", tableName, numCycles, average(createTimes))
	fmt.Printf("Average Read time for %s over %d cycles: %.2f seconds\n", tableName, numCycles, average(readTimes))
	fmt.Printf("Average Create time2 for %s over %d cycles: %.2f seconds\n", tableName, numCycles, average(createTimes2))
	fmt.Printf("Average Update time for %s over %d cycles: %.2f seconds\n", tableName, numCycles, average(updateTimes))
	fmt.Printf("Average Overall Update time for %s over %d cycles: %.2f seconds\n", tableName, numCycles, average(updateTimesOverall))
	fmt.Printf("Average Delete time for %s over %d cycles: %.2f seconds\n", tableName, numCycles, average(deleteTimes))
	fmt.Printf("Average total time for %s over %d cycles: %.2f seconds\n", tableName, numCycles, average(totalTimes))
}

func average(times []float64) float64 {
	var sum float64
	for _, t := range times {
		sum += t
	}
	return sum / float64(len(times))
}

func createTableLite(db *sql.DB, tableName, datatype string) {
	_, err := db.Exec(fmt.Sprintf("DROP TABLE IF EXISTS %s", tableName))
	if err != nil {
		log.Fatal(err)
	}

	_, err = db.Exec(fmt.Sprintf("CREATE TABLE %s (id INTEGER, value %s)", tableName, datatype))
	if err != nil {
		log.Fatal(err)
	}
}

func updateRecordLite(db *sql.DB, tableName, tableName2, datatype string) {
	_, err := db.Exec(fmt.Sprintf("UPDATE %s SET value = t2.value FROM %s t2 WHERE %s.id = t2.id", tableName, tableName2, tableName))
	if err != nil {
		log.Fatal(err)
	}
}

func tryDeleteAllRecordsLite(db *sql.DB, tableName string) {
	_, err := db.Exec(fmt.Sprintf("DELETE FROM %s", tableName))
	if err != nil {
		if !strings.Contains(err.Error(), "no such table") {
			log.Fatal(err)
		} else {
			fmt.Printf("Table '%s' does not exist\n", tableName)
		}
	}
}

func insertDataLite(db *sql.DB, tableName string) {
	csvFile := "data/" + tableName + ".csv"
	file, err := os.Open(csvFile)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	reader := csv.NewReader(file)
	columns, err := reader.Read()
	if err != nil {
		log.Fatal(err)
	}

	// Prepare the SQL statement for inserting data
	query := "INSERT INTO " + tableName + " (" + strings.Join(columns, ",") + ") VALUES ("

	for i := range columns {
		query += "?"
		if i < len(columns)-1 {
			query += ", "
		}
	}
	query += ")"
	stmt, err := db.Prepare(query)
	if err != nil {
		log.Fatal(err)
	}
	defer stmt.Close()

	tx, err := db.Begin()
	if err != nil {
		log.Fatal(err)
	}

	// Read and insert data from the CSV file
	for {
		row, err := reader.Read()
		if err == io.EOF {
			break
		} else if err != nil {
			log.Fatal(err)
		}

		args := make([]interface{}, len(columns))
		for i, value := range row {
			// Convert each CSV field to string
			args[i] = value
		}

		_, err = tx.Stmt(stmt).Exec(args...)
		if err != nil {
			log.Fatal(err)
		}
	}

	err = tx.Commit()
	if err != nil {
		log.Fatal(err)
	}
}

func readAllRecordsLite(db *sql.DB, tableName string) {
	rows, err := db.Query("SELECT * FROM " + tableName + " ORDER BY id DESC")
	if err != nil {
		log.Fatal(err)
	}
	defer rows.Close()

	for rows.Next() {
		// Read the data, but don't perform any additional actions
	}

	if err := rows.Err(); err != nil {
		log.Fatal(err)
	}
}
