def deleteUserSql(uid):
    templateSQL = """DELETE
FROM public.users
WHERE email = '%%%%@a.com';
"""
    return templateSQL.replace("%%%%", uid)

for i in range(1000):
    print(deleteUserSql("soma-stress-test-"+ str(i)))
