--adding the column status to user1 table to distinguish celebrities from regular people

ALTER TABLE User1
ADD Status NVARCHAR(20) DEFAULT 'Regular';

UPDATE User1
SET Status = 'Regular'
WHERE Status IS NULL;