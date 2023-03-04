"""Pendant Publishing edits multi-volume manuscripts for many authors. For each volume, they want a label that contains the author's name, the title of the work, and a volume number in the form Volume 9 of 9. For example, a set of three volumes requires three labels: Volume 1 of 3, Volume 2 of 3, and Volume 3 of 3. Design an application that reads records that contain an author's name, the title of the work, and the number of volumes. The application must read the records until eof is encountered and produce enough labels for each work."""

with open("PendantPublishing.txt", "r") as file:
  total_volumes = 0
  for line in file:
    total_volumes += 1

  file.seek(0)

  volume_number = 0
  for line in file:
    volume_number += 1
    data = line.split(",")
    print(f"VOLUME {volume_number} OF {total_volumes}")
    print(f"Author: {data[0]}")
    print(f"Title:{data[1]}")
    print(f"Number of Volumes:{data[2]}\n")

"""
Adams, A Complete History of the World, 10
Samuels, My Life of Crime, 2
Baum, Wizard Stories, 6 
"""