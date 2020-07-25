# Implementation: Tree

## Author: _Leo Kukharau_

## Challenge

- Create a `Node` class that has properties for the value stored in the node, the `left` child node, and the `right` child node.
- Create a `BinaryTree` class
  - Define a method for each of the depth first traversals called `preOrder`, `inOrder`, and `postOrder` which returns an array of the values, ordered appropriately.
- Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

- Create a `BinarySearchTree` class
  - Define a method named `add` that accepts a value, and adds a new node with that value in the correct location in the binary search tree.
  - Define a method named `contains` that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency

## API

- class `Node` - Class for the Node instances
- Class `Stack` - which implements Stack data structure with its common methods

  - `.is_empty()` - Method to check if Stack is empty;
  - `.push(value)` - Method takes any value as an argument and adds a new node with that value to the top of the stack;
  - `.pop()` - Method that removes the node from the top of the stack, and returns the node’s value;
  - `.peek()` - Method that returns the value of the node located on top of the stack, without removing it from the stack.

- class `Queue` - which implements Queue data structure with its common methods
  - `.is_empty()` - method to check if Queue is empty;
  - `.enqueue(value)` - method that takes any value as an argument and adds a new node with that value to the back of the queue;
  - `.dequeue()` - Method that removes the node from the front of the queue, and returns the node’s value;
  - `.peek()` - Method that returns the value of the node located in the front of the queue, without removing it from the queue.

<a href="./tree.py">Link to code</a>
