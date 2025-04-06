import random
import string
def create_rand_links(n):
    base_link = "https://chat.whatsapp.com/"
    final_text = ""

    #GVbDLUabCrG7uKrOjSGhs1#example of random chars

    def generate_random_string():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=22))
    for i in range(n):
        rand_link = base_link+generate_random_string()
        final_text += rand_link+"\n"

    with open("links.txt","w") as f:
        f.write(final_text)

create_rand_links(10_000)