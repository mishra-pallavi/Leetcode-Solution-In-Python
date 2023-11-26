# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

class Solution:
    def fizzBuzz(self, n: int):
            answer = []

            for i in range(1,n+1):
                divisibleby3 = i % 3 == 0
                divisibleby5 = i % 5 == 0

                if i % 3 == 0 and i % 5 == 0:
                    answer.append("FizzBuzz")
                elif divisibleby3:
                    answer.append("Fizz")
                elif divisibleby5:
                    answer.append("Buzz")
                else:
                    answer.append(str(i))

            return answer
    

solution_instance = Solution()

n_value = 5
result = solution_instance.fizzBuzz(n_value)
print(result)


# ["1","2","Fizz"]