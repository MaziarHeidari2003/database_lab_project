CREATE TRIGGER MakeCelebrity
ON Post
AFTER INSERT, UPDATE
AS
BEGIN
    DECLARE @PostAuthorID INT;
    DECLARE @PostCount INT;

    -- Get the AuthorID of the updated/inserted row
    SELECT @PostAuthorID = Author FROM inserted;

    -- Check if the updated post has 10 or more likes
    SELECT @PostCount = Likes FROM inserted;

    IF @PostCount >= 10
    BEGIN
        -- Update the author's status to celebrity
        UPDATE User1
        SET Status = 'Celebrity'
        WHERE ID = @PostAuthorID;
    END
END