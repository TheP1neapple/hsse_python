from tensor import Tensor
from matrix import Matrix

print(" Tensor Test ".center(50, "="))
print()

T = Tensor((3,3,3), [i for i in range(27)])

print(f"T is {T}")

print("\n" * 3)

print(" Matrix Test ".center(50, "="))
print()

M = Matrix((10, 10), list(range(100)))

print("1. M\n")
print(M)
print()

print("2. M[1, 1]\n")
print(M[1, 1])
print()

print("3. M[1]\n")
print(M[1])
print()

print("4. M[-1]\n")
print(M[-1])
print()

print("5. M[1:4]\n")
print(M[1:4])
print()

print("6. M[:4]\n")
print(M[:4])
print()

print("7. M[4:]\n")
print(M[4:])
print()

print("8. M[:]\n")
print(M[:])
print()

print("9. M[1:7:2]\n")
print(M[1:7:2])
print()

print("10. M[:, 1]\n")
print(M[:, 1])
print()

print("11. M[1:4, 1:4]\n")
print(M[1:4, 1:4])
print()

print("12. M[1:4, :4]\n")
print(M[1:4, :4])
print()

print("13. M[1:4, 4:]\n")
print(M[1:4, 4:])
print()

print("14. M[1:4, :]\n")
print(M[1:4, :])
print()

print("15. M[-1:]\n")
print(M[-1:])
print()

print("16. M[-2::-2]\n")
print(M[-2::-2])
print()

print("17. M[-2::-2, 1:4]\n")
print(M[-2::-2, 1:4])
print()

print("18. M[:, :]\n")
print(M[:, :])
print()

print("19. M[[1, 4]]\n")
print(M[[1, 4]])
print()

print("20. M[:, [1, 4]]\n")
print(M[:, [1, 4]])
print()

print("21. M[[1, 4], [1, 4]]\n")
print(M[[1,4], [1, 4]])
print()