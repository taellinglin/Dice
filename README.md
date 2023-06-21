```
  _____                            __  __              _   _______                _   _               
 |  __ \                          |  \/  |            (_) |__   __|              | | | |              
 | |  | | _ __ ___  __ _ _ __ ___ | \  / |  __ _  __ _ _  ___| |  ___   __ _  ___| |_| |__   ___ _ __ 
 | |  | || '__/ _ \/ _` | '_ ` _ \| |\/| | / _` |/ _` | |/ __| | / _ \ / _` |/ _ \ __| '_ \ / _ \ '__|
 | |__| || | |  __/ (_| | | | | | | |  | || (_| | (_| | | (__| || (_) | (_| |  __/ |_| | | |  __/ |   
 |_____(_)_|  \___|\__,_|_| |_| |_|_|  |_(_)__,_|\__, |_|\___|_(_)___/ \__, |\___|\__|_| |_|\___|_|   
                                                  __/ |                 __/ |                         
                                                 |___/                 |___/     
```
# 掷骰子可视化工具

这是一个使用Panda3D游戏引擎创建实时3D骰子滚动可视化的程序。该程序会随机选择房间、骰子模型和GLSL着色器，创建动态和视觉上吸引人的场景。

## 安装

在运行程序之前，您需要安装Panda3D游戏引擎。请按照Panda3D官方文档中提供的安装指南进行操作：[Panda3D安装指南](https://www.panda3d.org/manual/index.php/Installing_Panda3D)

## 使用方法

1. 克隆仓库：
   
   ```git clone https://github.com/taellinglin/Dice.git```

2. 安装所需依赖项（Panda3D已经安装）：
   - 不需要特定的Python依赖项，因为Panda3D包含了自己的Python解释器。

3. 添加房间和骰子模型：
   - 将您的房间的 `.blend` 文件放入 `rooms/` 目录中。
   - 将您的骰子的 `.blend` 文件放入 `dice/` 目录中。
   - 运行以下命令：
     ```blend2bam ./rooms/ ./rooms/*```
     和
     ```blend2bam ./dice/ ./dice/*```
     这将从文件夹中的 *.blend 文件创建 *.bam 文件。

4. 添加GLSL着色器：
   - 使用GLSL版本150编写您的GLSL着色器。
   - 将 `.frag.glsl` 和 `.vert.glsl` 着色器文件放入 `shaders/` 目录中。

5. 运行程序：
   - 打开终端或命令提示符。
   - 切换到项目目录。
   - 执行以下命令：
     ```
     python main.py
     ```

6. 欣赏可视化效果：
   - 该程序将生成随机组合的房间、骰子和着色器，每次运行时都会产生独特的可视化效果。

## 未来改进

将来，该程序计划加入以下功能：

- 随机化的音效与可视化效果相伴。
- 纹理以增强房间和骰子的渲染效果。
- 视频效果以获得更沉浸式的可视化效果。
- 响应输入声音的音频反应功能。

欢迎通过添加更多资源、着色器或其他功能来为项目做出贡献！

## 许可证

该项目采用Ling Lin许可证（LLL）进行许可。有关更多详细信息，请参阅READLING文件。

```
  _____                            __  __              _   _______                _   _               
 |  __ \                          |  \/  |            (_) |__   __|              | | | |              
 | |  | | _ __ ___  __ _ _ __ ___ | \  / |  __ _  __ _ _  ___| |  ___   __ _  ___| |_| |__   ___ _ __ 
 | |  | || '__/ _ \/ _` | '_ ` _ \| |\/| | / _` |/ _` | |/ __| | / _ \ / _` |/ _ \ __| '_ \ / _ \ '__|
 | |__| || | |  __/ (_| | | | | | | |  | || (_| | (_| | | (__| || (_) | (_| |  __/ |_| | | |  __/ |   
 |_____(_)_|  \___|\__,_|_| |_| |_|_|  |_(_)__,_|\__, |_|\___|_(_)___/ \__, |\___|\__|_| |_|\___|_|   
                                                  __/ |                 __/ |                         
                                                 |___/                 |___/     
```

# Dice Rolling Visualizer

This is a visualizer program that utilizes the Panda3D game engine to create a real-time 3D visualization of rolling dice in different rooms. The program randomly selects a room, a dice model, and GLSL shaders to create a dynamic and visually appealing scene.

## Installation

Before running the program, you need to install the Panda3D game engine. Follow the installation instructions provided by the official Panda3D documentation: [Panda3D Installation Guide](https://www.panda3d.org/manual/index.php/Installing_Panda3D)

## Usage

1. Clone the repository:
 
 ```git clone https://github.com/taellinglin/Dice.git```

2. Install the required dependencies (Panda3D is already installed):
- No specific Python dependencies are needed, as Panda3D includes its own Python interpreter.

3. Add your room and dice models:
- Place your `.blend` files for rooms in the `room/` directory.
- Place your `.blend` files for dice in the `dice/` directory.
- Run this:
    ```blend2bam ./room/ ./room/*```
    and
    ```blend2bam ./dice/ ./dice/*```
    That will create *.bam files from the *.blend files in the folders.

4. Add GLSL shaders:
- Write your GLSL shaders with GLSL version 150.
- Place your `.frag.glsl` and `.vert.glsl` shader files in the `shaders/` directory.

5. Run the program:
- Open a terminal or command prompt.
- Navigate to the project directory.
- Execute the following command:
  ```
  python main.py
  ```

6. Enjoy the visualizations:
- The program will generate random combinations of rooms, dice, and shaders, resulting in unique visualizations each time you run it.

## Future Enhancements

In the future, the program aims to incorporate the following features:

- Randomized audio effects to accompany the visualizations.
- Textures to enhance the rendering of rooms and dice.
- Video effects for more immersive visualizations.
- Audio reactive features that respond to the input sound.

Feel free to contribute to the project by adding more assets, shaders, or additional features!

## License

The project is licensed under the Ling Lin License(LLL). See the READLING file for more details.
