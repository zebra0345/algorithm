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

	var inputWord string
	fmt.Fscan(reader, &inputWord)

	alpha := []string{"dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="}
	for _, val := range alpha {
		if strings.Contains(inputWord, val) {
			inputWord = strings.ReplaceAll(inputWord, val, "#")
		}
	}

	fmt.Fprint(writer, len(inputWord))
}
