--like and unlike peocedure
CREATE PROCEDURE AddLike
    @UserID bigINT,
    @PostID bigINT
AS
BEGIN
    INSERT INTO PostLikes (UserID, PostID) VALUES (@UserID, @PostID);
END




CREATE PROCEDURE RemoveLike
    @UserID INT,
    @PostID INT
AS
BEGIN
    DELETE FROM PostLikes WHERE UserID = @UserID AND PostID = @PostID;
END


