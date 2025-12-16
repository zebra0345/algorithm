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

	var T int
	fmt.Fscan(reader, &T)

	for i := 0; i < T; i++ {
		var money int
		fmt.Fscan(reader, &money)

		var q, d, n, p int
		q = money / 25
		money = money % 25
		d = money / 10
		money = money % 10
		n = money / 5
		money = money % 5
		p = money / 1
		fmt.Fprintln(writer, q, d, n, p)
	}
}
