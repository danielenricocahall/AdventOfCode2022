from typing import List, Optional


def find_marker_of_interest(datastream_buffer: List[str], marker_window_size: int) -> Optional[int]:
    for index in range(len(datastream_buffer)):
        duplicates = len(set(datastream_buffer[index:index+marker_window_size])) != marker_window_size
        if not duplicates:
            return index + marker_window_size


if __name__ == "__main__":
    with open('./input.txt') as f:
        datastream_buffer = list(next(f))
    protocol_packet_size = 4
    protocol_message_size = 14
    print(find_marker_of_interest(datastream_buffer, protocol_packet_size))
    print(find_marker_of_interest(datastream_buffer, protocol_message_size))



