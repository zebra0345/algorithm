package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	var s string
	var num int

	fmt.Fscan(reader, &s, &num)
	result, _ := strconv.ParseInt(s, num, 64)

	fmt.Fprint(writer, result)
}
