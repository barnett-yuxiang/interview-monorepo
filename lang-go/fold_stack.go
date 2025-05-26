package main

type Node struct {
	Name     string
	Count    int
	Children map[string]*Node
}

func NewNode(name string) *Node {
	return &Node{
		Name:     name,
		Children: make(map[string]*Node),
	}
}

func insertStack(root *Node, stack []string) {
	curr := root
	for _, frame := range stack {
		if curr.Children[frame] == nil {

		}
	}
}
