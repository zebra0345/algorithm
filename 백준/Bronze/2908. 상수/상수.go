package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func swap(s string) string{
	runes := []rune(s)
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	var a string
	var b string

	fmt.Fscan(reader, &a, &b)
	num1, _ := strconv.Atoi(swap(a))
	num2, _ := strconv.Atoi(swap(b))

	if (num1) > int(num2) {
		fmt.Fprintln(writer, num1)
	} else {
		fmt.Fprintln(writer, num2)
	}
	
}