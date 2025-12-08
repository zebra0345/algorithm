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

	var word string
	fmt.Fscan(reader, &word)

	var newWord string
	for i := len(word) - 1; i >= 0; i-- {
		newWord += string(word[i])
	}

	if word == newWord {
		fmt.Fprint(writer, 1)
	} else {
		fmt.Fprint(writer, 0)
	}
}
