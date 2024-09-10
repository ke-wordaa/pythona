import pyautogui
import time

def find_and_move_all():
        matches_a = list(pyautogui.locateAllOnScreen('a.png'))
        
        if matches_a:
            print(f"找到 {len(matches_a)} 个 'a.png' 的位置")
           
            for match in matches_a:
                    x, y = match.left + match.width / 2, match.top + match.height / 2
                    print(f"文字 'a.png' 的位置：({x}, {y})")

                    pyautogui.moveTo(x, y)       
                    time.sleep(0.5)         
                    pyautogui.leftClick()  # 执行左键点击

                    # 寻找并移动到单个 'bb.png' 的位置
                    match_bb = pyautogui.locateOnScreen('b.png')

                    if match_bb:
                        w, z = match_bb.left + match_bb.width / 2, match_bb.top + match_bb.height / 2
                        print(f"'b.png' 的位置：({w}, {z})")
                        pyautogui.moveTo(w, z)
                        pyautogui.leftClick()
        pyautogui.moveTo(1428.5, 728.0)
        pyautogui.scroll(-400)
        time.sleep(1)
        find_and_move_all()
if __name__ == "__main__": 
    i = 1
    while i != 0:
        time.sleep(1)
        print(i)
        i -= 1
    
    find_and_move_all()
