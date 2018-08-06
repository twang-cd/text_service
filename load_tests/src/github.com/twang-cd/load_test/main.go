package main

import (
	"fmt"
	"os"
	"strings"
	"time"

	vegeta "github.com/tsenart/vegeta/lib"
)

func Attack(name, baseUrl, version, query string) {
	rate := uint64(200)
	duration := 60 * time.Second

	targeter := vegeta.NewStaticTargeter(vegeta.Target{
		Method: "GET",
		URL:    fmt.Sprintf("http://%s/alphacheck/%s/%s", baseUrl, version, query),
	})

	attacker := vegeta.NewAttacker()
	var results vegeta.Results
	var metrics vegeta.Metrics
	for res := range attacker.Attack(targeter, rate, duration, name) {
		metrics.Add(res)
		results.Add(res)
	}
	metrics.Close()

	reporter := vegeta.NewPlotReporter(fmt.Sprintf("http://%s/alphacheck/%s/%s test: ", baseUrl, version, query), &results)
	f, err := os.Create(fmt.Sprintf("%s.html", name))
	if err != nil {
		panic(err)
	}
	reporter.Report(f)

	fmt.Printf("Test: %s, 99th percentile: %s\n", name, metrics.Latencies.P99)
}

func main() {
	baseUrl := os.Args[1]
	fmt.Printf("baseUrl: %s\n", baseUrl)

	query1 := "abcdefghijklmnopqrstuvwxyz"
	Attack("short-v1", baseUrl, "v1", query1)
	Attack("short-v2", baseUrl, "v2", query1)

	query2 := strings.Repeat(query1, 50)
	Attack("long-v1", baseUrl, "v1", query2)
	Attack("long-v2", baseUrl, "v2", query2)
}
