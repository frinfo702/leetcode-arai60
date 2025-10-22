struct Solution;

impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        let mut right = (nums.len() - 1) as i32;
        let mut left = 0;

        while left <= right {
            if nums[left as usize] == target {
                return left;
            } else if nums[left as usize] > target {
                return left;
            } else if nums[right as usize] == target {
                return right;
            } else if nums[right as usize] < target {
                return right + 1;
            }

            right -= 1;
            left += 1;
        }

        return right + 1;
    }
}

fn main() {
    println!("{:?}", Solution::search_insert(vec![1, 3, 5, 6], 2));
    println!("{:?}", Solution::search_insert(vec![1, 3], 2));
}
