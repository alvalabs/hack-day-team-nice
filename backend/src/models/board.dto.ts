import { ApiModelProperty } from "@nestjs/swagger";
import BoardFeatureDto from "./board-feature.dto";
import { GameObjectDto } from "./game-object.dto";

export class BoardDto {
  @ApiModelProperty({
    description:
      "A unique id of the board to use when querying just a specific board.",
  })
  id: number;
  @ApiModelProperty({
    description: "The width of the board.",
  })
  width: number;
  @ApiModelProperty({
    description: "The height of the board.",
  })
  height: number;
  @ApiModelProperty({
    description:
      "The minimum delay (in ms) required between moves of the same bot.",
  })
  minimumDelayBetweenMoves: number;
  @ApiModelProperty({
    isArray: true,
    type: GameObjectDto,
    description: "All game objects currently on the board.",
  })
  gameObjects: GameObjectDto[];
  @ApiModelProperty({
    isArray: true,
    type: BoardFeatureDto,
    description:
      "The features that are are enabled for this board along with their configuration.",
  })
  features: BoardFeatureDto[];
}
