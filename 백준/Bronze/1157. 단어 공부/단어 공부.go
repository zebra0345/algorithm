package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()
	var words string
	fmt.Fscan(reader, &words)

	words = strings.ToLower(words)
	check := make(map[string]int)
	for i := 0; i < len(words); i++ {
		check[string(words[i])]++
	}

	max := 0
	result := ""
	count := 0
	for key, val := range check {
		if max < val {
			max = val
			result = key
			count = 1
		} else if val == max {
			count++
		}
	}
	if count >= 2 {
		fmt.Fprint(writer, "?")
	} else {
		fmt.Fprint(writer, strings.ToUpper(result))
	}
}
