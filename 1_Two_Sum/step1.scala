object Solution:
  def twoSum(nums: Array[Int], target: Int): Array[Int] =
    val visited = scala.collection.mutable.Map[Int, Int]()
    scala.util.boundary:
      for (index <- nums.indices) {
        val complement = target - nums(index)
        if visited.contains(complement) then
          scala.util.boundary.break(Array(visited(complement), index))
        visited(nums(index)) = index
      }
      Array()

@main def run(): Unit =
  val result = Solution.twoSum(Array(2, 7, 11, 15), 9)
  println(result.mkString("[", ", ", "]"))
