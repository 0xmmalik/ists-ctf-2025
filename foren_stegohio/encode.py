from PIL import Image


def encode_flag_in_gif(flag, input_gif, output_gif):
    bit_mapping = {"00": 0, "01": 10, "10": 100, "11": 110}

    binary_flag = ''.join(f'{ord(c):08b}' for c in flag)
    bit_pairs = [binary_flag[i:i + 2] for i in range(0, len(binary_flag), 2)]
    delays = [bit_mapping[b] for b in bit_pairs]

    with Image.open(input_gif) as gif:
        frames = []
        num_frames = gif.n_frames

        if len(delays) > num_frames:
            print("[!] Not enough frames. Repeating frames to fit the encoding.")

        for i in range(len(delays)):
            gif.seek(i % num_frames)
            frame = gif.copy()
            frames.append(frame)

        frames[0].save(output_gif, save_all=True, append_images=frames[1:],
                       duration=delays, loop=0)
    print(f"[✔] Flag encoded into GIF. Saved as {output_gif}")


def extract_flag_from_gif(stego_gif):
    reverse_mapping = {0: "00", 10: "01", 100: "10", 110: "11"}

    with Image.open(stego_gif) as gif:
        binary_data = ""

        for i in range(gif.n_frames):
            gif.seek(i)
            delay = gif.info.get('duration', 0)
            print(delay)
            bit_pair = reverse_mapping.get(delay, "??")
            binary_data += bit_pair

        print(binary_data)

        flag = ''.join(chr(int(binary_data[i:i + 8], 2)) for i in range(0, len(binary_data), 8))

    print(f"[✔] Extracted Flag: {flag}")
    return flag


# flag = "ISTS{g1f_m3_4_br3ak}"
# encode_flag_in_gif(flag, "ohio.gif", "stegohio.gif")
print(extract_flag_from_gif("stegohio.gif"))
