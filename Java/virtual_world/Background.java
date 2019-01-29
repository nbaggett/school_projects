import java.util.List;
import java.util.Scanner;

import processing.core.PImage;

final class Background
{
   private static final int BGND_NUM_PROPERTIES = 4;
   private static final int BGND_ID = 1;
   private static final int BGND_COL = 2;
   private static final int BGND_ROW = 3;

   private String id;
   private List<PImage> images;
   private int imageIndex = 0;

   public Background(String id, List<PImage> images)
   {
      this.id = id;
      this.images = images;
   }

   public List<PImage> getImages() {
      return images;
   }

   public int getImageIndex() {
      return imageIndex;
   }

   public static boolean parse(ImageStore imageStore, String [] properties,
                                   WorldModel world)
   {
      if (properties.length == BGND_NUM_PROPERTIES)
      {
         Point pt = new Point(Integer.parseInt(properties[BGND_COL]),
                 Integer.parseInt(properties[BGND_ROW]));
         String id = properties[BGND_ID];
         world.setBackground(pt,
                 new Background(id, imageStore.getImageList(id)));
      }

      return properties.length == BGND_NUM_PROPERTIES;
   }
}
