import cv2
import numpy as np


def count_bin(img, num_bin):

  h = img.shape[0]
  w = img.shape[1]
  d = img.shape[2]

  res = np.zeros(dtype=np.int32, shape=[d, num_bin])

  for i in range(h):
    for j in range(w):
      for di in range(d):
        res[di][img[i,j,di] // (256 // num_bin)] += 1


  return res


def draw_hist(img, num_bin):
  bin_count = count_bin(img, num_bin)

  hist_h = 420
  hist_w = 390
  hist_d = img.shape[2]

  hist_img = np.zeros(dtype=np.uint8, shape=[hist_h, hist_w, hist_d])

  bin_w = hist_w / num_bin
  h_ratio = (hist_h) / (np.max(bin_count, axis=1))


  for d in range(bin_count.shape[0]):
    for bin in range(1, bin_count.shape[1]):
      cv2.line(hist_img, (np.int(bin_w*bin), hist_h - np.int(bin_count[d, bin] * h_ratio[d])),
               (np.int(bin_w*(bin-1)), hist_h - np.int(bin_count[d, bin-1] * h_ratio[d])), (255,255,255))



  return hist_img

def main():
  img = cv2.imread('blackhole.jpg')

  hist_img = draw_hist(img, num_bin=16)

  cv2.imshow('image', img)
  cv2.imshow('histogram', hist_img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

if __name__ == '__main__':
  main()