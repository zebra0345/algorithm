package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n int
	fmt.Fscan(reader, &n)

	// 위쪽 (1, 3, 5, 7, 9)
	for i := 0; i < n; i++ {
		for j := 0; j < n-1-i; j++ {
			fmt.Fprint(writer, " ")
		}
		for j := 0; j < 2*i+1; j++ {
			fmt.Fprint(writer, "*")
		}
		fmt.Fprintln(writer)
	}

	for i := n - 2; i >= 0; i-- {
		for j := 0; j < n-1-i; j++ {
			fmt.Fprint(writer, " ")
		}
		for j := 0; j < 2*i+1; j++ {
			fmt.Fprint(writer, "*")
		}
		fmt.Fprintln(writer)
	}
}
