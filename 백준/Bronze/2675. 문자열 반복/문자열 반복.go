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
	var t int

	fmt.Fscan(reader, &t)

	for i := 0; i < t; i++ {
		var r int
		var s string
		fmt.Fscan(reader, &r, &s)

		newS := make([]string, 0)
		for j := 0; j < len(s); j++ {
			newS = append(newS, strings.Repeat(string(s[j]), r))
		}
		fmt.Fprintln(writer, strings.Join(newS, ""))
	}

}
