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

	var s string
	fmt.Fscan(reader, &s)

	pos := make([]int, 26)

	for i := 0; i < 26; i++ {
		pos[i] = -1
	}

	for i := 0; i < len(s); i++ {
		idx := s[i] - 'a'
		if pos[idx] == -1 {
			pos[idx] = i
		}
	}

	for i := 0; i < 26; i++ {
		fmt.Fprint(writer, pos[i], " ")
	}
}
