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
	var a, b int
	fmt.Fscan(reader, &a, &b)

	if a > b {
		fmt.Fprint(writer, ">")
	} else if a < b {
		fmt.Fprint(writer, "<")
	} else {
		fmt.Fprint(writer, "==")
	}
}