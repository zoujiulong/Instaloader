import instaloader
import os
import time
import argparse
import tqdm
def download_instagram_posts(username,target_username, save_dir,sleep):
    # 创建 Instaloader 实例
    L = instaloader.Instaloader()
    L.load_session_from_file(username)  # 直接加载 session
    target_dir = os.path.join(save_dir, target_username)
    os.makedirs(target_dir, exist_ok=True)
    print(target_dir)
    # 获取用户 profile
    profile = instaloader.Profile.from_username(L.context, target_username)
    # 下载所有帖子
    for post in tqdm(profile.get_posts(),desc="Download Numbers"):
        L.download_post(post, target=target_dir.strip())
        time.sleep(sleep)
    print(f"✅ {target_username} 的所有帖子已下载到 {target_dir}！")
if __name__=='__main__':
    parser = argparse.ArgumentParser(description="instagram download parameters")
    parser.add_argument("-username", type=str, help="Own username")
    parser.add_argument("-targetUsername", type=str, help="target username")
    parser.add_argument("-saveDir", type=str, help="save directory")
    parser.add_argument("-sleep", type=int, help="sleep time/s")
    args = parser.parse_args()
    download_instagram_posts(args.username,args.targetUsername,args.saveDir,args.sleep)