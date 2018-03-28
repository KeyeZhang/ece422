import binascii

base_url = "http://72.36.89.11:9999/mp3/awzhang3/?"

import urllib2
def get_status(u):
    req = urllib2.Request(u)
    try:
        f = urllib2.urlopen(req)
        return f.code
    except urllib2.HTTPError, e:
        # print e.read().strip()
        return e.code

with open("3.2.3_ciphertext.hex") as fd:
    text = fd.readlines()[0];

blocks = []
for i in range(len(text)/32):
    blocks.append(text[i*32:(i+1)*32])

padding = range(0x10, 0, -1)

def extract_plaintext_from_block(block_idx, blocks):

    c_curr = blocks[block_idx]
    c_prev = []
    for i in range(0x10):
        c_prev.append(int(blocks[block_idx - 1][i*2:i*2+2], 16))

    p_ = [0]*16
    i_ = [0]*16

    # SOLVE FOR POSITION
    for position in range(0xF, -1, -1):

        p_prime = [0]*position + padding[:0x10-position]

        c_prime = [0]*16
        for i in range(position, 0x10):
            if i > position:
                c_prime[i] = p_prime[i] ^ i_[i]

        # print("POSITION: " + str(position))
        # print(p_)
        # print(i_)
        # print("")

        # print(p_prime)
        # print(c_prime)
        # print("")

        # SOLVE FOR VAL
        val = False
        for i in range(0x100):
            c_prime[position] = i
            arg = ''.join('{:02x}'.format(c) for c in c_prime)
            status = get_status(base_url + arg + c_curr)
            if status == 404:
                val = True
                break

        if not val:
            print("FAILED TO FIND CORRECT PADDING")
            exit(1)

        # SOLVE FOR I2 and P2
        i_[position] = c_prime[position] ^ p_prime[position]
        p_[position] = c_prev[position] ^ i_[position]

    # print("FINISHED")
    return p_


plain_text = []
for i in range(1, len(blocks)):
    print("extracting block: " + str(i-1))
    p_ = extract_plaintext_from_block(i, blocks)
    plain_text += p_

human_readable_plain_text = ''.join(chr(p) for p in plain_text)
print(human_readable_plain_text)

"""
e802778b05ba1e2dc438e0ee56c176b2
ce1b0d852a239275c43700384408e19d
7bae7801d666e32b38f9853da21e1ae1
71e72a765a9bb3f2820319d69383d046
463460e4feadd475c611372e173be6ed
e08bd96df450e270397251b32a0a62f9
2eb3a18eac5e0d09cd00193b7bdefa86
1e4929ed6aedc5fb81573fa1bfd8b839
"""
