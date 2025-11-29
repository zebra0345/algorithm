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

	line, _ := reader.ReadString('\n')
	result := strings.Fields(line)
	fmt.Fprint(writer, len(result))
}
