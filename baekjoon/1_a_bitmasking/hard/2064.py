import sys

input = sys.stdin.readline

def ip_to_num(address):
    add_list = address.split('.')
    address_num = 0
    for i in range(4):
        digit = 3 - i
        temp = int(add_list[i]) << (8 * digit)
        address_num += temp
    return address_num

def num_to_ip(address):
    add_list = []
    address_updated = address
    for i in range(4):
        digit = 3 - i
        address_now = (address_updated >> (8 * digit))
        add_list.append(str(address_now))
        address_updated -= (address_now << (8 * digit))
    return '.'.join(add_list)

def run_program():
    # N개의 ip 주소 bin로 입력받기
    N = int(input().strip())
    bin_addresses = []
    for _ in range(N):
        bin_addresses.append(ip_to_num(input().strip()))
    # mask 구하기
    mask_result = (1 << 32) - 1
    for i in range(1, N):
        temp_result = ~(bin_addresses[i] ^ bin_addresses[i-1])
        mask_result &= temp_result
    mask_result = (1 << 32) | mask_result
    # print(bin(mask_result))
    zero_flag = False
    # 연속 형태로 최종 변환
    for i in range(32):
        digit = 31 - i
        if not mask_result & (1 << digit):
          zero_flag = True
        if zero_flag:
            mask_result &= ~(1 << digit)  
    network_mask = mask_result - (1 << 32)
    # print(bin(network_mask))
    # mask 이용 네트워크 주소 구하기
    network_address = bin_addresses[0] & network_mask
    # 결과 출력
    print(num_to_ip(network_address))
    print(num_to_ip(network_mask))
  
run_program()