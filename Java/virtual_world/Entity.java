import processing.core.PImage;
import java.util.List;

public abstract class Entity
{
   private String id;
   private Point position;
   private List<PImage> images;

   public Entity(String id, Point position, List<PImage> images)
   {
      this.id = id;
      this.position = position;
      this.images = images;
   }

   public String getId() { return id; }

   public Point getPosition()
   {
      return position;
   }

   public List<PImage> getImages()
   {
      return images;
   }

   public void setPosition(Point position)
   {
      this.position = position;
   }

   public int getImageIndex() { return 0; }

   public void remove(WorldModel world) {
      Point temp = position;
      if (world.withinBounds(position)
              && world.getOccupancyCell(position) != null) {
         Entity entity = world.getOccupancyCell(position);

         /* this moves the entity just outside of the grid for
            debugging purposes */
         setPosition(new Point(-1, -1));
         world.entities.remove(entity);
         world.setOccupancyCell(temp, null);
      }
   }

   public static PImage getCurrentImage(Object entity)
   {
      if (entity instanceof Background)
      {
         return ((Background)entity).getImages()
                 .get(((Background)entity).getImageIndex());
      }
      else if (entity instanceof Entity)
      {
         return ((Entity)entity).getImages().get(((Entity)entity).getImageIndex());
      }
      else
      {
         throw new UnsupportedOperationException(
                 String.format("getCurrentImage not supported for %s",
                         entity));
      }
   }
}