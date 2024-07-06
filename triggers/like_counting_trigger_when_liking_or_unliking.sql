--like counting trigger when liking or unliking

CREATE TRIGGER UpdateLikesCount
ON PostLikes
AFTER INSERT
AS
BEGIN
    UPDATE Post
    SET Likes = Likes + 1
    WHERE ID = (SELECT PostID FROM inserted);
END



CREATE TRIGGER UpdateLikesCountRemovigLike
ON PostLikes
AFTER DELETE
AS
BEGIN
    DECLARE @PostID BIGINT;
    DECLARE @PostCount INT;

    -- Get the PostID of the deleted row
    SELECT @PostID = PostID FROM deleted;

    -- Check if the updated post has 10 or more likes
    SELECT @PostCount = COUNT(*) FROM PostLikes WHERE PostID = @PostID;

    -- Update the post's LikesCount
    UPDATE Post
    SET Likes = @PostCount
    WHERE ID = @PostID;
END