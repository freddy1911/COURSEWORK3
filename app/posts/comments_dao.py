from app.posts.comments_class import Comment
from app.utils import open_json_read


class CommentsDAO:

    def get_comments_by_post_id(self, post_id):
        """ Получение комментарием по номеру поста"""
        file = 'data/comments.json'
        data = open_json_read(file)
        posts = []
        for post in data:
            if post_id == post["post_id"]:
                posts.append(Comment(
                    post["post_id"],
                    post["commenter_name"],
                    post["comment"],
                    post["pk"]
                ))
        return posts
