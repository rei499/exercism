"""Functions to manage and organize queues at Chaitana's roller coaster."""

def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """
    :param express_queue (list): The names in the Fast-track queue.
    :param normal_queue (list): The names in the normal queue.
    :param ticket_type (int): Type of ticket. 1 = express, 0 = normal.
    :param person_name (str): The name of person to add to a queue.
    :returns (list): The (updated) queue the name was added to.
    """
    if ticket_type == 1: 
        express_queue.append(person_name)
        return express_queue
    if ticket_type == 0: 
        normal_queue.append(person_name)
        return normal_queue
    return None
    
def find_my_friend(queue, friend_name):
    """
    :param queue (list): The names in the queue.
    :param friend_name (str): The name of friend to find.
    :returns (int): The index at which the friends name was found.
    """
    
    friend = queue.index(friend_name)
    return friend if friend_name in queue  else None

def add_me_with_my_friends(queue, index, person_name):
    """
    :param queue (list): The names in the queue.
    :param index (int): The index at which to add the new name.
    :param person_name (str): The name to add.
    :returns list: The queue updated with new name.
    """

    queue.insert(index, person_name)
    return queue

def remove_the_mean_person(queue, person_name):
    """
    :param queue (list): The names in the queue.
    :param person_name (str): The name of mean person.
    :returns (list): The queue updated with the mean persons name removed.
    """

    queue.remove(person_name)
    return queue

def how_many_namefellows(queue, person_name):
    """
    :param queue (list): The names in the queue.
    :param person_name (str): The name you wish to count or track.
    :returns (int): The number of times the name appears in the queue.
    """

    return queue.count(person_name)

def remove_the_last_person(queue):
    """
    :param queue (list): The names in the queue.
    :returns (str): The name that has been removed from the end of the queue.
    """

    last_person = queue[-1]
    queue.pop()
    return last_person

def sorted_names(queue):
    """
    :param queue (list): The names in the queue.
    :returns(list): A copy of the queue in alphabetical order.
    """

    return sorted(queue)