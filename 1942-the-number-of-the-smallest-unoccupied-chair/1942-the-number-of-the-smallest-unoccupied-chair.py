class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        # Store events with (time, friend_id, type_of_event)
        events = []
        n = len(times)
        
        for friend_id, (arrival, leaving) in enumerate(times):
            events.append((arrival, friend_id, 'arrive'))
            events.append((leaving, friend_id, 'leave'))
        
        # Sort the events: first by time, and in case of tie, leave event before arrive
        events.sort(key=lambda x: (x[0], x[2] == 'arrive'))

        # Min-heap for available chairs
        available_chairs = []
        # Map to store which chair each friend is sitting on
        occupied_chairs = {}

        # Start with chair 0 being the first available one
        current_chair = 0

        # Process all the events
        for time, friend_id, event_type in events:
            if event_type == 'arrive':
                # If there are available chairs, use the smallest one, otherwise take the next new chair
                if available_chairs:
                    chair = heapq.heappop(available_chairs)
                else:
                    chair = current_chair
                    current_chair += 1
                
                # Assign this chair to the arriving friend
                occupied_chairs[friend_id] = chair
                
                # If the arriving friend is the target friend, return the chair
                if friend_id == targetFriend:
                    return chair
            else:  # event_type == 'leave'
                # Friend is leaving, so release their chair
                chair = occupied_chairs[friend_id]
                heapq.heappush(available_chairs, chair)
        