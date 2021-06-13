
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;

public class UploadLog : MonoBehaviour
{
    private Queue<string> logs = new Queue<string>();
    private LogInfo cache = new LogInfo();

    private string ip = "127.0.0.1";
    private string username = "test";
    private string password = "test";
    private string projectName = "项目测试";
    public int uid = -1;//空白

    private void Awake()
    {
        logs.Enqueue($"login?username={username}&password={password}");
        Application.logMessageReceived += (string condition, string stackTrace, LogType type) =>
        {
            if (type != LogType.Warning)
            {
                cache.level = type.GetHashCode();
                cache.info = condition + ">>>" + stackTrace;
                cache.time = Time.time.ToString();
                logs.Enqueue("[" + JsonUtility.ToJson(cache) + "]");
            }
        };
        for (int i = 0; i < 30; i++)
        {
            Debug.Log("Test Log");
            Debug.Log("Test Log1");
        }
    }
    private void Start()
    {
        EFramework.Network.Http.HttpHelper.HttpGetRequestAsync($"http://{ip}/" + logs.Dequeue(), (string x) => { if (x.Length >= 3 && x.Substring(0, 3) == "uid") uid = int.Parse(x.Substring(3)); else Debug.LogWarning(x); });
    }
    private void Update()
    {
        if (logs.Count > 0 && uid >= 0)
        {
            EFramework.Network.Http.HttpHelper.HttpGetRequestAsync($"http://{ip}/insert?name={projectName}&uid={uid}&log=" + logs.Dequeue(), (string x) => { Debug.LogWarning(x); });
        }
    }
}
public class LogInfo
{
    public int level;
    public string time;
    public string info;
}