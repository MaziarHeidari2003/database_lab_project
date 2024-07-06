CREATE PROCEDURE GetCommentsByPostID
    @PostID BIGINT
AS
BEGIN
SELECT  C.content,u.first_name, C.published_date
    FROM Comment AS C join user1 as u on c.commenter=u.id 
    WHERE C.Post = @PostID;
END
