CREATE TABLE PostLikes (
    UserID bigINT,
    PostID bigINT,
    PRIMARY KEY (UserID, PostID),
    FOREIGN KEY (UserID) REFERENCES User1(ID),
    FOREIGN KEY (PostID) REFERENCES Post(ID)
);


