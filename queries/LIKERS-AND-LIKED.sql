SELECT
    SourceMember.DisplayName AS Liker,
    TargetMember.DisplayName AS Liked
FROM Likes
INNER JOIN Members AS SourceMember
    ON Likes.SourceMemberId = SourceMember.Id
INNER JOIN Members AS TargetMember
    ON Likes.TargetMemberId = TargetMember.Id
ORDER BY SourceMember.DisplayName