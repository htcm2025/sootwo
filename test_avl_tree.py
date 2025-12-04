from avl_tree import AVLTree


def test_insert_and_search():
    print("Testing insert and search...")
    avl = AVLTree()
    values = [10, 20, 30, 40, 50, 25]

    for val in values:
        avl.insert(val)

    for val in values:
        assert avl.search(val), f"Value {val} should be found"

    assert not avl.search(100), "Value 100 should not be found"
    print("✓ Insert and search test passed")


def test_inorder_traversal():
    print("\nTesting inorder traversal...")
    avl = AVLTree()
    values = [10, 20, 30, 40, 50, 25]

    for val in values:
        avl.insert(val)

    result = avl.inorder()
    expected = sorted(values)
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Inorder traversal: {result}")


def test_balance():
    print("\nTesting AVL balance property...")
    avl = AVLTree()

    # Insert values that would create unbalanced BST
    for i in range(1, 8):
        avl.insert(i)

    assert avl.is_balanced(), "Tree should be balanced"
    print(f"✓ Tree is balanced with height: {avl.get_height()}")


def test_rotations():
    print("\nTesting rotations...")
    avl = AVLTree()

    # Test right rotation (Left-Left case)
    avl.insert(30)
    avl.insert(20)
    avl.insert(10)

    assert avl.root.value == 20, "Root should be 20 after right rotation"
    assert avl.root.left.value == 10, "Left child should be 10"
    assert avl.root.right.value == 30, "Right child should be 30"
    print("✓ Right rotation works correctly")

    # Test left rotation (Right-Right case)
    avl2 = AVLTree()
    avl2.insert(10)
    avl2.insert(20)
    avl2.insert(30)

    assert avl2.root.value == 20, "Root should be 20 after left rotation"
    assert avl2.root.left.value == 10, "Left child should be 10"
    assert avl2.root.right.value == 30, "Right child should be 30"
    print("✓ Left rotation works correctly")


def test_delete():
    print("\nTesting delete operation...")
    avl = AVLTree()
    values = [10, 20, 30, 40, 50, 25]

    for val in values:
        avl.insert(val)

    # Delete a leaf node
    avl.delete(50)
    assert not avl.search(50), "Value 50 should be deleted"
    assert avl.is_balanced(), "Tree should remain balanced after deletion"
    print("✓ Leaf node deletion works")

    # Delete a node with one child
    avl.delete(40)
    assert not avl.search(40), "Value 40 should be deleted"
    assert avl.is_balanced(), "Tree should remain balanced after deletion"
    print("✓ Node with one child deletion works")

    # Delete a node with two children
    avl.delete(30)
    assert not avl.search(30), "Value 30 should be deleted"
    assert avl.is_balanced(), "Tree should remain balanced after deletion"
    print("✓ Node with two children deletion works")

    remaining = avl.inorder()
    print(f"✓ Remaining values: {remaining}")


def test_traversals():
    print("\nTesting different traversals...")
    avl = AVLTree()
    values = [50, 30, 70, 20, 40, 60, 80]

    for val in values:
        avl.insert(val)

    inorder = avl.inorder()
    preorder = avl.preorder()
    postorder = avl.postorder()

    print(f"  Inorder: {inorder}")
    print(f"  Preorder: {preorder}")
    print(f"  Postorder: {postorder}")

    assert inorder == sorted(values), "Inorder should be sorted"
    print("✓ All traversals work correctly")


if __name__ == "__main__":
    print("=" * 50)
    print("AVL Tree Test Suite")
    print("=" * 50)

    test_insert_and_search()
    test_inorder_traversal()
    test_balance()
    test_rotations()
    test_delete()
    test_traversals()

    print("\n" + "=" * 50)
    print("All tests passed! ✓")
    print("=" * 50)
