def createUserSql(uid):
    templateSQL = """INSERT INTO public.users (uid, "createdAt", "updatedAt", nickname, email, hash, avatar, "githubId", "googleId",
                          "kakaoId", verified, verify_token, badges, blog_link, github_link, groups, status_quo)
VALUES (DEFAULT, '2022-11-22 17:40:15.000'::timestamp(3), '2022-11-22 17:40:53.000'::timestamp(3), '%%%%'::text,
        '%%%%@a.com'::text,
        '$argon2id$v=19$m=4096,t=3,p=1$bJ3BGOhuJrCcReKgZoVFWg$7quenF4gX8sB8k+YPqC4d8qWHCGMwuCePMWO7MQ4UfM'::text,
        1::integer, null::text, null::text, null::text, true, null, '{}', ' ', ' ', '{}', ' ');
"""
    return templateSQL.replace("%%%%", uid)
#print(createUserSql("somatest1"))

for i in range(1000):
    print(createUserSql("soma-stress-test-"+ str(i)))
