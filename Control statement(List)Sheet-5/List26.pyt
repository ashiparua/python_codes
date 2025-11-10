#  The Exam Result Analyzer
n=int(input())
marks = list(map(int, input().split()))
passed = 0
failed = 0
for m in marks:
    if m >= 35:
        passed += 1
    else:
        failed += 1
print("Passed:", passed)
print("Failed:", failed)    
        