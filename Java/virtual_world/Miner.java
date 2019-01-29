import processing.core.PImage;
import java.util.List;

public class Miner extends AnimatedEntity {

    public Miner(String id, Point position, List<PImage> images, int actionPeriod, int animationPeriod)
    {
        super(id, position, images, actionPeriod, animationPeriod);
    }

    public void executeActivity(WorldModel world, ImageStore imageStore, EventScheduler scheduler)
    {

    }
}
