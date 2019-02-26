/*Description
There are two properties in the node student id and scores, to ensure that each student will have at least 5 points, find the average of 5 highest scores for each person.

Example
Given results = [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]*/

/**
 * Definition for a Record
 * class Record {
 *     public int id, score;
 *     public Record(int id, int score){
 *         this.id = id;
 *         this.score = score;
 *     }
 * }
 */

import java.util.*;
public class Solution {
    /**
     * @param results a list of <student_id, score>
     * @return find the average of 5 highest scores for each person
     * Map<Integer, Double> (student_id, average_score)
     */
    public Map<Integer, Double> highFive(Record[] results) {
        Map<Integer, Double> result = new HashMap<Integer, Double>();
        Map<Integer, PriorityQueue<Integer>> map = new HashMap<Integer, PriorityQueue<Integer>>();
        int k = 5;

        // NOW SCAN
        for (Record r : results) {
            if (!map.containsKey(r.id)) { // Works like getOrDefault()
                Queue pq = new PriorityQueue<Integer>();
                map.put(r.id, pq);
            }
            map.get(r.id).add(r.score); // Add current record's score
            if (map.get(r.id) > k) map.get(r.id).poll(); // Remove last if more than k
        }

        // NOW GATHER STATISTICS
        for (Map.Entry<Integer, PriorityQueue<Integer>) entry : map.entrySet) {
            int id = entry.getKey();
            PriorityQueue<Integer> q = entry.getValue();
            int qSize = q.size();
            double average = 0;
            while (!q.isEmpty()) {
                average += q.poll();
            }
            average /= qSize;
            result.put(id, average);
        }

        return result;
    }
}