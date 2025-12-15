package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	var n int
	fmt.Fscan(reader, &n)
	defer writer.Flush()
	board := make([][]bool, 100)
	for i := 0; i < 100; i++ {
		board[i] = make([]bool, 100)
	}

	for i := 0; i < n; i++ {
		var x, y int
		fmt.Fscan(reader, &x, &y)

		for r := x; r < x+10; r++ {
			for c := y; c < y+10; c++ {
				board[r][c] = true
			}
		}
	}

	area := 0
	for i := 0; i < 100; i++ {
		for j := 0; j < 100; j++ {
			if board[i][j] {
				area++
			}
		}
	}
	fmt.Println(area)
}
