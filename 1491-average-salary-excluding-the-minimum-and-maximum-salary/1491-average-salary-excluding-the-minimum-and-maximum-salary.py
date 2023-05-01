class Solution:
    def average(self, salary: List[int]) -> float:
        print(sum(salary),max(salary)+min(salary))
        return (sum(salary)-(max(salary)+min(salary)))/(len(salary)-2)