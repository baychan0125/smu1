import os
import pickle

FILENAME = 'score.bin'


def input_scores():
    scores = []
    i = 1
    while True:
        try:
            score = int(input(f"#{i}? "))
            if score < 0:
                break
            scores.append(score)
            i += 1
        except ValueError:
            print("숫자를 입력하세요.")
    return scores


def show_scores(scores):
    print("[점수 출력]")
    print("개인점수:", ' '.join(map(str, scores)))
    avg = sum(scores) / len(scores)
    print(f"평균: {avg:.1f}")

def save_scores(scores):
    with open(FILENAME, 'wb') as f:
        pickle.dump(scores, f)


def load_scores():
    with open(FILENAME, 'rb') as f:
        return pickle.load(f)


def main():
    if os.path.exists(FILENAME):
        print("[파일 읽기]")
        scores = load_scores()
    else:
        print("[점수 입력]")
        scores = input_scores()
        save_scores(scores)

    show_scores(scores)

if __name__ == '__main__':
    main()
