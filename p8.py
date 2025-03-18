class Comment:
    def __init__(self, user, comment):
        self.user = user
        self.comment = comment

    def __str__(self):
        return f"{self.user}: {self.comment}"


class Post:
    _id_counter = 1

    def __init__(self, content, user):
        self.post_id = Post._id_counter
        Post._id_counter += 1
        self.content = content
        self.user = user
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def display_post(self):
        print(f"Post ID: {self.post_id}")
        print(f"User: {self.user}")
        print(f"Content: {self.content}")
        print("Comments:")
        for comment in self.comments:
            print(f"  - {comment}")


class SocialMediaSystem:
    def __init__(self):
        self.posts = []

    def create_post(self, content, user):
        new_post = Post(content, user)
        self.posts.append(new_post)
        print(f"Post created with ID: {new_post.post_id}")

    def view_posts(self):
        if not self.posts:
            print("No posts available.")
        else:
            for post in self.posts:
                post.display_post()
                print("-" * 40)

    def add_comment(self, post_id, comment_content, user):
        if post:
            new_comment = Comment(user, comment_content)
            post.add_comment(new_comment)
            print("Comment added successfully.")
        else:
            print("Post not found.")


    def main():
        system = SocialMediaSystem()

        while True:
            print("\nSocial Media Simulator")
            print("1. Create a post")
            print("2. View posts")
            print("3. Add a comment")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                user = input("Enter your username: ")
                content = input("Enter the content of the post: ")
                system.create_post(content, user)
            elif choice == "2":
                system.view_posts()
            elif choice == "3":
                try:
                    post_id = int(input("Enter the post ID to comment on: "))
                    user = input("Enter your username: ")
                    comment_content = input("Enter your comment: ")
                    system.add_comment(post_id, comment_content, user)
                except ValueError:
                    print("Invalid post ID.")
            elif choice == "4":
                print("Exiting the simulator. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


    if __name__ == "__main__":
        main()
        post = next((p for p in self.posts if p.post_id == post_id), None)
